##parameters=
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.utils import decode
from Products.CMFDefault.utils import getBrowserCharset

atool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IActionsTool',
                                  # BBB: fallback for CMF 2.2 instances
                                  getToolByName(script, 'portal_actions'))
caltool = getToolByName(script, 'portal_calendar', None)
mtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IMembershipTool',
                                  # BBB: fallback for CMF 2.2 instances
                                  getToolByName(script, 'portal_membership'))
ptool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IPropertiesTool')
utool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IURLTool',
                                  # BBB: fallback for CMF 2.2 instances
                                  getToolByName(script, 'portal_url'))
wtool = getToolByName(script, 'portal_workflow')
uidtool = getToolByName(script, 'portal_uidhandler', None)
syndtool = getToolByName(script, 'portal_syndication', None)
portal_object = utool.getPortalObject()
isAnon = mtool.isAnonymousUser()
member = mtool.getAuthenticatedMember()

if not 'charset' in (context.REQUEST.RESPONSE.getHeader('content-type') or ''):
    # Some newstyle views set a different charset - don't override it.
    # Oldstyle views need the default_charset.
    default_charset = ptool.getProperty('default_charset', None)
    if default_charset:
        context.REQUEST.RESPONSE.setHeader('content-type',
                                    'text/html; charset=%s' % default_charset)

message = context.REQUEST.get('portal_status_message')
if message and isinstance(message, str):
    # portal_status_message uses always the browser charset.
    message = message.decode(getBrowserCharset(context.REQUEST))

globals = {'utool': utool,
           'mtool': mtool,
           'atool': atool,
           'wtool': wtool,
           'syndtool': syndtool,
           'caltool_installed': caltool is not None,
           'uidtool_installed': uidtool is not None,
           'portal_object': portal_object,
           'portal_title': portal_object.Title(),
           'object_title': context.Title(),
           'object_description': context.Description(),
           'portal_url': utool(),
           'member': member,
           'membername': isAnon and 'Guest' or (member.getProperty('fullname')
                                                or member.getId()),
           'membersfolder': mtool.getMembersFolder(),
           'isAnon': isAnon,
           'wf_state': wtool.getInfoFor(context, 'review_state', ''),
           'show_actionicons': ptool.getProperty('enable_actionicons'),
           'status_message': message}

return decode(globals, context)
